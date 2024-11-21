'use strict';

document.getElementById('searchForm').addEventListener('submit', async function(event) {
      event.preventDefault();

      const query = document.getElementById('query').value;
      const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

      try {
          const response = await fetch(url);
          if (!response.ok) throw new Error(
                  `HTTP error! Status: ${response.status}`);

          const data = await response.json()
          console.log(data);

          const resultsElement = document.getElementById('results');
          resultsElement.textContent = JSON.stringify(data, null, 2);
      } catch (error) {
          console.error('Error fetching data:', error);
          document.getElementById('results').textContent = `Error: ${error.message}`;
      }
});