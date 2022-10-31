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

var camera, renderer, scene, particleSystem, baseParticle, mouse;
window.onload = function () {
  mouse = [window.innerWidth / 2, window.innerHeight / 2];
  renderer = new THREE.WebGLRenderer({ antialias: true });
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(20, window.innerWidth / window.innerHeight, 0.1, 1000);
  renderer.setSize(window.innerWidth, window.innerHeight);
  document.body.appendChild(renderer.domElement);
  camera.position.z = 50;
  scene.background = new THREE.Color(0x333344);
  canvas = document.querySelector('#b canvas');

  baseParticle = new THREE.PlaneGeometry(1, 1, 1);
  baseParticle.applyMatrix(new THREE.Matrix4().makeRotationFromEuler(new THREE.Euler(0, 0, Math.PI / 4)));
  for (var i = 0; i < baseParticle.vertices.length; i++) {
    if (Math.round(baseParticle.vertices[i].y) != 0) {
      baseParticle.vertices[i].x = 0;
      baseParticle.vertices[i].z = 0;
    }
  }
  baseParticle.mergeVertices();
  baseParticle.verticesNeedUpdate = true;
  baseParticle = new THREE.Mesh(baseParticle, new THREE.MeshBasicMaterial({ color: 0xffffff, emissive: 0x555555 }));
  particleSystem = new ParticleSystem(99);

  render();
};

window.onresize = function () {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
};

window.onmousemove = function (e) {
  mouse = [e.clientX, e.clientY];
};

function randomFloat(a, b) {
  var r = Math.random() * (b - a) + a;
  return r;
}

function partToHex(part) {
  var h = part.toString(16);
  return h.length == 1 ? "0" + h : h;
}

console.log(partToHex(255));

var color;
function FireParticle() {
  this.direction;
  this.scaleSpeed;
  this.curAge;

  this.parent;

  this.obj;
  this.colorRamp = [[255, 255, 0], [255, 136, 34], [255, 17, 68], [153, 136, 136]];

  this.update = function () {
    if (Math.abs(this.parent.pos.x - this.obj.position.x) > 10 || Math.abs(-this.parent.pos.y - this.obj.position.y) > 10) {
      this.obj.scale.x *= .8;
      this.obj.scale.y *= .8;
      this.obj.scale.z *= .8;
    }

    var point = this.curAge / 40;
    var pointRem = point % 1;

    if (Math.round(point) >= this.colorRamp.length - 1) {
      color = this.colorRamp[this.colorRamp.length - 1];
    } else {
      color = [Math.floor(this.colorRamp[Math.floor(point)][0] * (1 - pointRem) + this.colorRamp[Math.floor(point) + 1][0] * pointRem), Math.floor(this.colorRamp[Math.floor(point)][1] * (1 - pointRem) + this.colorRamp[Math.floor(point) + 1][1] * pointRem), Math.floor(this.colorRamp[Math.floor(point)][2] * (1 - pointRem) + this.colorRamp[Math.floor(point) + 1][2] * pointRem)];
    }

    color = partToHex(color[0]) + partToHex(color[1]) + partToHex(color[2]);
    color = parseInt(color, 16);

    this.obj.material.color.setHex(color);

    this.curAge++;

    if (this.obj.scale.x < .01) {
      this.init();
    }

    this.obj.position.x += this.direction.x;
    this.obj.position.y += this.direction.y;
    this.obj.position.z += this.direction.z;

    this.obj.scale.x *= this.scaleSpeed;
    this.obj.scale.y *= this.scaleSpeed;
    this.obj.scale.z *= this.scaleSpeed;
  };

  this.init = function () {
    this.direction = new THREE.Vector3(randomFloat(-.01, .01), randomFloat(.01, .1), randomFloat(-.01, .01));
    this.scaleSpeed = randomFloat(.8, .99);
    this.curAge = 0;

    if (this.obj != undefined) {
      scene.remove(this.obj);
    }

    this.obj = baseParticle.clone();
    this.obj.position.set(this.parent.obj.position.x + randomFloat(-.2, .2), this.parent.obj.position.y, this.parent.obj.position.z + randomFloat(-.2, .2));
    this.obj.scale.set(1, 2, 1);
    this.obj.material = this.obj.material.clone();
    // var size = randomFloat(.5, 1);
    // this.obj.scale.set(size, 2*size, size);

    for (var i = 0; i < randomFloat(0, 100); i++) {
      this.update();
    }

    scene.add(this.obj);
  };




}

function ParticleSystem(size) {
  this.particles = [];
  this.obj = new THREE.Group();

  this.p = new THREE.Vector3();
  this.d;
  this.dis;
  this.pos = new THREE.Vector3(0, 0, 0);

  this.init = function () {
    for (var i = 0; i < size; i++) {
      this.particles.push(new FireParticle());
      this.particles[i].parent = this;
      this.particles[i].init();
    }

    scene.add(this.obj);
  };
  this.init();

  this.update = function () {
    this.p.set(mouse[0] / window.innerWidth * 2 - 1, mouse[1] / window.innerHeight * 2 - 1, .5);
    this.p.unproject(camera);
    this.d = this.p.sub(camera.position).normalize();
    this.dis = -camera.position.z / this.d.z;
    this.pos = camera.position.clone().add(this.d.multiplyScalar(this.dis));

    this.obj.position.x = this.pos.x;
    this.obj.position.y = -this.pos.y;

    for (var i = 0; i < this.particles.length; i++) {
      this.particles[i].update();
    }

    this.obj.rotation.y += .03;
  };
}

function render() {
  requestAnimationFrame(render);
  renderer.render(scene, camera);
  particleSystem.update();
}



