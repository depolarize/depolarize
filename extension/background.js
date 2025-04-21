chrome.runtime.onMessage.addListener(async (msg) => {
  if (msg.type === 'PAGE_TEXT') {
    try {
      // 1) Fetch & capture the Response object
      const res = await fetch('http://localhost:5001/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify({ text: msg.payload })
      });

      // 2) Log status
      console.log('[De‑Polarize] HTTP status:', res.status, res.statusText);

      // 3) Parse JSON once
      const data = await res.json();
      console.log('[De‑Polarize] parsed data:', data);

      // 4) Store the entire payload (bias, alignment, summary)
      await chrome.storage.local.set(data);

    } catch (err) {
      console.error('[De‑Polarize] error in fetch:', err);
    }
  }
});
