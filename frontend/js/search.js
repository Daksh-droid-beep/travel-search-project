const searchForm = document.getElementById("searchForm");
const searchInput = document.getElementById("searchQuery");
const searchTypeSelect = document.getElementById("searchType");

const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const pageInfo = document.getElementById("pageInfo");

let limit = 6;
let offset = 0;
let lastQuery = "";
let lastType = "all";

searchForm.addEventListener("submit", (e) => {
  e.preventDefault();
  offset = 0;
  lastQuery = searchInput.value.trim();
  lastType = searchTypeSelect.value;
  fetchResults();
});

prevBtn.addEventListener("click", () => {
  if (offset >= limit) {
    offset -= limit;
    fetchResults();
  }
});

nextBtn.addEventListener("click", () => {
  offset += limit;
  fetchResults();
});

async function fetchResults() {
  if (!lastQuery) {
    showError("Enter a search query");
    return;
  }

  showLoading();

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/search?q=${encodeURIComponent(
        lastQuery
      )}&search_type=${lastType}&limit=${limit}&offset=${offset}`
    );

    if (!response.ok) {
      throw new Error("API error");
    }

    const data = await response.json();

    // ✅ CORRECTED LINES
    renderResults(data.results);

    pageInfo.textContent = `Showing ${
      offset + 1
    }–${Math.min(offset + limit, data.total_results)} of ${
      data.total_results
    }`;

    prevBtn.disabled = offset === 0;
    nextBtn.disabled = offset + limit >= data.total_results;
  } catch (err) {
    console.error(err);
    showError("Backend not reachable");
  }
}
