<script>
  const faders = document.querySelectorAll('.fade-in');
  window.addEventListener('scroll', () => {
    faders.forEach(fade => {
      const rect = fade.getBoundingClientRect();
      if (rect.top < window.innerHeight - 100) {
        fade.classList.add('visible');
      }
    });
  });
</script>
