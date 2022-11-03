/*!
* Start Bootstrap - Blog Home v5.0.8 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
/**
 * I prefer to style the border's `border-image`, and I avoid using pseudo
 * elements when possible, so the styles may be applied to block level
 * elements, for use where an <hr> would be non-semantic.
 */

/* Inline XML data URI fix */
/* Some browsers (most browsers) don't render inline XML data URI's unless they are escaped. */

$(document).ready(function(){
    
  $(document).mousemove(function(e){
      var mouseX = e.pageX;
      var mouseY = e.pageY;

      $('.cursor').css({
          left: mouseX + "px",
          top : mouseY + "px"
      })
  })
})


class Particle{
  constructor(id, opt) {
    this.box = document.getElementById(id);
    this.number = opt.number || 100;
    this.colors = this.handleArrayParams(opt.colors) || ['#400606', '#c7b4aa', '#ffffff'];
    this.width = opt.width || 15;
    this.height = opt.height || 7; 
    this.duration = opt.duration || 6000;
    this.delay = opt.delay || 6000;
  }
  handleArrayParams(arr) {
    return Array.isArray(arr) && arr.length > 0 && arr.every(el => el[0]==='#') ? arr : false;
  }
  getRandom(max, min = 0) {
    min = Math.ceil(min);
    max = Math.floor(max+1);
    return Math.floor(Math.random() * (max - min)) + min;
  }
  getRange(num, range = 0.5){
    const symbol = Math.random() > 0.5 ? +1 : -1;
    return num + this.getRandom(Math.floor(num * range)) * symbol;
  }
  start() {
    for(let i = 0; i < this.number; i++){
      const temp = document.createElement('span');
      temp.style.cssText += `
        position: absolute;
        transform-style: preserve-3d;
        animation-timing-function: cubic-bezier(${this.getRandom(3)*0.1}, 0, 1, 1);
        animation-iteration-count: infinite;
        width: ${this.getRange(this.width, 0.7)}px;
        height: ${this.getRange(this.height, 0.7)}px;
        top: -${this.width * 2}px;
        left: calc(${this.getRandom(100)}% - ${this.width*0.5}px);
        background-color: ${this.colors[this.getRandom(this.colors.length-1)]};
        animation-name: fallen_${this.getRandom(5, 1)};
        animation-duration: ${this.getRange(this.duration)}ms;
        animation-delay: ${this.getRange(this.delay)}ms;
       `;
      this.box.append(temp);
    }
  }
}

const party = new Particle('particle', { number: 200, colors: ['#ffca76', '#ffb9b9', '#fff180'] });
party.start();


// Created for an Articles on:
// https://www.html5andbeyond.com/bubbling-text-effect-no-canvas-required/

jQuery(document).ready(function ($) {
  // Define a blank array for the effect positions. This will be populated based on width of the title.
  var bArray = [];
  // Define a size array, this will be used to vary bubble sizes
  var sArray = [4, 6, 8, 10];

  // Push the header width values to bArray
  for (var i = 0; i < $(".bubbles").width(); i++) {
    bArray.push(i);
  }

  // Function to select random array element
  // Used within the setInterval a few times
  function randomValue(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
  }

  // setInterval function used to create new bubble every 350 milliseconds
  setInterval(function () {
    // Get a random size, defined as variable so it can be used for both width and height
    var size = randomValue(sArray);
    // New bubble appeneded to div with it's size and left position being set inline
    // Left value is set through getting a random value from bArray
    $(".bubbles").append(
    '<div class="individual-bubble" style="left: ' +
    randomValue(bArray) +
    "px; width: " +
    size +
    "px; height:" +
    size +
    'px;"></div>');


    // Animate each bubble to the top (bottom 100%) and reduce opacity as it moves
    // Callback function used to remove finsihed animations from the page
    $(".individual-bubble").animate(
    {
      bottom: "100%",
      opacity: "-=0.7" },

    3000,
    function () {
      $(this).remove();
    });

  }, 350);
});