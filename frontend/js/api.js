// Live backend URL (production)
const BASE_URL = "https://travel-search-project-3.onrender.com";

/**
 * Fetch with retry (handles Render cold start)
 */
async function fetchWithRetry(url, options = {}, retries = 2, delay = 2000) {
  try {
    const response = await fetch(url, options);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return await response.json();
  } catch (error) {
    if (retries > 0) {
      console.warn("Backend waking up, retrying...");
      await new Promise(resolve => setTimeout(resolve, delay));
      return fetchWithRetry(url, options, retries - 1, delay);
    }
    throw error;
  }
}

/**
 * Search API
 */
async function searchAPI(query, searchType, limit, offset) {
  const url =
    `${BASE_URL}/api/search` +
    `?q=${encodeURIComponent(query)}` +
    `&search_type=${searchType}` +
    `&limit=${limit}` +
    `&offset=${offset}`;

  return fetchWithRetry(url);
}

/**
 * Admin: manual sync
 */
async function manualSync() {
  const url = `${BASE_URL}/api/admin/sync`;
  return fetchWithRetry(url, { method: "POST" });
}
