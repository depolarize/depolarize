chrome.runtime.onMessage.addListener(async (msg) => {
  if (msg.type === 'PAGE_TEXT') {
    try {
      const res = await fetch('http://localhost:5001/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({ text: msg.payload })
      });

      console.log('[Depolarize] HTTP status:', res.status, res.statusText);

      const data = await res.json();
      console.log('[Depolarize] parsed data:', data);

      // store payload (bias, alignment, summary) in local storage
      await chrome.storage.local.set(data);

    } catch (err) {
      console.error('[Depolarize] error in fetch:', err);
    }
  }
});

// clear previous analysis wen tabs switched
chrome.tabs.onActivated.addListener(async ({ tabId }) => {
  await chrome.storage.local.clear();
  console.log('[Depolarize] cleared old data on tab switch');

  chrome.scripting.executeScript({
    target: { tabId },
    files: ['content.js']
  });
});