const loading = document.getElementById('loading-gif');

if(loading) {
   setTimeout(() => {
      window.location.replace('/foods');
   }, 3000);
}