const resultsContainer = document.getElementById("resultsContainer");
const messageBox = document.getElementById("messageBox");
const resultMeta = document.getElementById("resultMeta");

function showLoading() {
  resultsContainer.innerHTML = "";
  messageBox.innerHTML =
    `<div class="alert alert-secondary">Loading...</div>`;
}

function showError(msg) {
  resultsContainer.innerHTML = "";
  messageBox.innerHTML =
    `<div class="alert alert-danger">${msg}</div>`;
}

function renderResults(results) {
  resultsContainer.innerHTML = "";
  messageBox.innerHTML = "";

  if (!results || results.length === 0) {
    messageBox.innerHTML =
      `<div class="alert alert-info">No results found</div>`;
    return;
  }

  results.forEach(item => {
    const col = document.createElement("div");
    col.className = "col-md-4";

    const title = item.name || item.city || "Unknown";
    const description = item.description || "No description available";

    col.innerHTML = `
      <div class="card h-100 shadow-sm">
        <div class="card-body">
          <h5>${title}</h5>
          <p>${description}</p>
          <span class="badge bg-primary">${item.type}</span>
        </div>
      </div>
    `;

    resultsContainer.appendChild(col);
  });
}
