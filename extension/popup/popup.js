document.addEventListener('DOMContentLoaded', async () => {
    const data = await chrome.storage.local.get(['bias', 'alignment', 'summary', 'raw']);
    document.getElementById('bias').innerText = data.bias;
    document.getElementById('alignment').innerText = data.alignment;
    document.getElementById('summary').innerText = data.summary;
});