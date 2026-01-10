const BASE_URL = "http://127.0.0.1:8000";

async function searchAPI(query, searchType, limit, offset) {
    const response = await fetch(
        `${BASE_URL}/api/search?q=${encodeURIComponent(query)}&search_type=${searchType}&limit=${limit}&offset=${offset}`
    );
    return response.json();
}
