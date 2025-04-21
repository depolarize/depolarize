chrome.storage.local.clear(() => {
    console.log('[Depolarize] cleared previous data');

    let paras = Array.from(document.querySelectorAll('article p'));
    if (!paras.length) paras = Array.from(document.body.querySelectorAll('p'));
    const text = paras.length
        ? paras.map(p => p.innerText).join('\n\n')
        : document.body.innerText;

    console.log('[Depolarize] sending text to background…');
    chrome.runtime.sendMessage({ type: 'PAGE_TEXT', payload: text });
});