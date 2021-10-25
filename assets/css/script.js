//jquery goes here
$(function(){

  
})
function carouselMargin(){
  let pic = $(".active").children();
  let picWid = pic.width()
  $(".carousel-item > img").each(function(){

  console.log(pic)
  
  console.log(picWid)
  screenWidth = window.innerWidth
  console.log(screenWidth+ "   "+ picWid)
  picMargin = (screenWidth-picWid)
  console.log(picMargin)
  
  $(this).css("margin-left",picMargin/2)

  })
  
  }



$(window).resize(carouselMargin())

function openForm() {
    document.getElementById("myForm").style.display = "block";
  }
  
  function closeForm() {
    document.getElementById("myForm").style.display = "none";
  }