document.addEventListener('DOMContentLoaded', () => {
    const loader = document.getElementById('loader');
    const content = document.getElementById('content');
    const biasFill = document.getElementById('bias-fill');
    const biasText = document.getElementById('bias');
    const biasDesc = document.getElementById('bias-intensity')
    const mark = document.getElementById('alignment-marker');
    const alignText = document.getElementById('alignment');
    const summary = document.getElementById('summary');
    const articleTextDiv = document.getElementById('article-text'); // Add this line
    const toggleBtn = document.getElementById('toggle-article-text');

    let articleTextVisible = false;

    function getBiasIntensity(val) {
        if (val <= 3) return 'Minimal emotional intensity';
        if (val <= 6) return 'Moderate emotional intensity';
        if (val <= 8) return 'High emotional intensity';
        return 'Extreme emotional intensity';
    }

    function showData(data) {
        const b = Number(data.bias) * 10 || 0;
        const roundedBias = Math.round(b * 100) / 100; 
        const pct = Math.min(Math.max(b, 0), 10) * 10;
        biasFill.style.width = pct + '%';
        biasText.textContent = roundedBias;

        biasDesc.textContent = getBiasIntensity(b);

        const order = [
            'highly conservative',
            'somewhat conservative',
            'neutral',
            'somewhat liberal',
            'highly liberal'
        ];
        const idx = order.indexOf((data.alignment || '').toLowerCase());
        const pos = idx >= 0 ? (idx / (order.length - 1)) * 100 : 50;
        mark.style.left = pos + '%';
        alignText.textContent = data.alignment || '';

        summary.textContent = data.summary || '';

        articleTextDiv.textContent = data.articleText || ''; 
        loader.style.display = 'none';
        content.style.display = 'block';
    }

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            articleTextVisible = !articleTextVisible;
            articleTextDiv.style.display = articleTextVisible ? 'block' : 'none';
            toggleBtn.textContent = articleTextVisible ? 'Hide article text' : 'Show article text';
        });
    }

    chrome.storage.local.get(
        ['bias', 'alignment', 'summary', 'articleText'], 
        d => {
            if (d.bias || d.alignment || d.summary) {
                showData(d);
            }
        }
    );

    chrome.storage.onChanged.addListener((changes, area) => {
        if (
            area === 'local' &&
            (changes.bias || changes.alignment || changes.summary || changes.articleText) 
        ) {
            chrome.storage.local.get(
                ['bias', 'alignment', 'summary', 'articleText'],
                showData
            );
        }
    });
});