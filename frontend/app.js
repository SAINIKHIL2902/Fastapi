let currentExerciseId = 'ex01';
let exercisesCache = {};

async function initPlatform() {
  const modulesListEl = document.getElementById('modules-list');

  try {
    const res = await fetch('/api/modules/');
    if (!res.ok) throw new Error('Failed to fetch modules');
    const data = await res.json();
    const modules = data.modules || [];

    modulesListEl.innerHTML = '';
    modules.forEach((mod, idx) => {
      const card = document.createElement('div');
      card.className = `module-card ${idx === 0 ? 'active' : ''}`;
      card.innerHTML = `
        <div class="module-header">
          <span class="module-weeks">${mod.weeks}</span>
          <span class="module-diff">${mod.difficulty}</span>
        </div>
        <h3 class="module-title">${mod.title}</h3>
        <p class="module-desc">${mod.description}</p>
        <div class="module-project">🏆 ${mod.project}</div>
      `;
      card.addEventListener('click', () => {
        document.querySelectorAll('.module-card').forEach((c) => c.classList.remove('active'));
        card.classList.add('active');
        loadModuleExercises(mod);
      });
      modulesListEl.appendChild(card);
    });

    if (modules.length > 0) {
      loadModuleExercises(modules[0]);
    }
  } catch (err) {
    modulesListEl.innerHTML = `
      <div style="color: #ef4444; padding: 1rem; font-size: 0.85rem;">
        Could not connect to FastAPI backend API at /api/modules.<br>
        Ensure the backend server is running on port 8000.
      </div>
    `;
  }
}

function loadModuleExercises(module) {
  const exercises = module.exercises || [];
  const activeModTag = document.getElementById('active-mod-tag');
  activeModTag.textContent = module.weeks;

  if (exercises.length > 0) {
    const ex = exercises[0];
    currentExerciseId = ex.id;
    exercisesCache[ex.id] = ex;
    displayExercise(ex);
  } else {
    document.getElementById('exercise-title').textContent = `${module.title} — Capstone Milestone`;
    document.getElementById('exercise-instructions').textContent = `Complete ${module.project}. Build and deploy this milestone using the patterns learned in this module.`;
    document.getElementById('code-editor').value = `# ${module.project}\n# Implement your milestone code here.\n`;
    document.getElementById('evaluation-badge').textContent = 'Milestone Project';
    document.getElementById('evaluation-badge').className = 'badge';
  }
}

function displayExercise(ex) {
  document.getElementById('exercise-title').textContent = ex.title;
  document.getElementById('exercise-instructions').innerHTML = ex.instructions.replace(/`([^`]+)`/g, '<code>$1</code>');
  document.getElementById('code-editor').value = ex.starter_code;
  const badge = document.getElementById('evaluation-badge');
  badge.textContent = 'Awaiting Submission';
  badge.className = 'badge';
  document.getElementById('terminal-output').textContent = 'Run your solution above to see automated test results.';
}

document.getElementById('reset-code-btn')?.addEventListener('click', () => {
  if (exercisesCache[currentExerciseId]) {
    displayExercise(exercisesCache[currentExerciseId]);
  }
});

document.getElementById('submit-code-btn')?.addEventListener('click', async () => {
  const code = document.getElementById('code-editor').value;
  const badge = document.getElementById('evaluation-badge');
  const terminal = document.getElementById('terminal-output');
  const statusMsg = document.getElementById('status-msg');

  badge.textContent = 'Testing...';
  badge.className = 'badge';
  statusMsg.textContent = 'Executing tests in isolated subprocess...';
  terminal.textContent = 'Running test harness...';

  try {
    const res = await fetch(`/api/exercises/${currentExerciseId}/submit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code })
    });

    const result = await res.json();

    if (result.status === 'passed') {
      badge.textContent = 'PASSED (100/100)';
      badge.className = 'badge passed';
      statusMsg.textContent = 'Congratulations! All automated assertions passed.';
      terminal.textContent = result.stdout || 'Tests completed successfully with exit code 0.';
    } else {
      badge.textContent = 'FAILED (0/100)';
      badge.className = 'badge failed';
      statusMsg.textContent = 'Verification failed. Inspect the traceback in the console below.';
      terminal.textContent = (result.stderr || '') + '\n' + (result.stdout || '');
    }
  } catch (err) {
    badge.textContent = 'ERROR';
    badge.className = 'badge failed';
    statusMsg.textContent = 'Failed to communicate with submission runner.';
    terminal.textContent = String(err);
  }
});

document.addEventListener('DOMContentLoaded', initPlatform);
