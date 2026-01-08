const BASE_URL = "https://travel-search-project-3.onrender.com";

async function searchAPI(query, searchType, limit, offset) {
  const response = await fetch(
    `${BASE_URL}/api/search?q=${encodeURIComponent(query)}&search_type=${searchType}&limit=${limit}&offset=${offset}`
  );
  return response.json();
}
