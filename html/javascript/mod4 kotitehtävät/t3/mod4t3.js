'use strict';

document.getElementById('searchForm').addEventListener('submit', async function(event) {
      event.preventDefault();

      const query = document.getElementById('query').value;
      const url = `https://api.tvmaze.com/search/shows?q=${encodeURIComponent(query)}`;

      const resultsContainer = document.getElementById('results');
      resultsContainer.innerHTML = '';

      try {
          const response = await fetch(url);
          if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);

          const data = await response.json()
          console.log(data);

          data.forEach(tvShow => {
              const show = tvShow.show;

              const article = document.createElement('article');

              const h2 = document.createElement('h2');
              h2.textContent = show.name;
              article.appendChild(h2);

              const link = document.createElement('a');
              link.href = show.url;
              link.target = '_blank';
              link.textContent = 'View Details';
              article.appendChild(link);

              if (show.image?.medium) {
                  const img = document.createElement('img');
                  img.src = show.image.medium;
                  img.alt = show.name;
                  article.appendChild(img);
              }

              const summaryDiv = document.createElement('div');
              summaryDiv.innerHTML = show.summary || 'No summary available.';
              article.appendChild(summaryDiv);

              resultsContainer.appendChild(article);
          });

      } catch (error) {
          console.error('Error fetching data:', error);
          resultsContainer.textContent = `Error: ${error.message}`;
      }
});