document.addEventListener('DOMContentLoaded', function() {
  const button = document.getElementById('animate-button')
  button.addEventListener('click', function() {
    button.classList.remove('animate')
    void button.offsetWidth
    button.classList.add('animate')
  })
})
