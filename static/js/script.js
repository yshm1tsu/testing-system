function copyToClipboard(code) {
    const el = document.createElement('textarea')
    el.style.position = 'absolute'
    el.style.left = '-9999px'
    el.value = code
    document.body.appendChild(el)
    el.select()
    document.execCommand('copy')
    document.body.removeChild(el)
}