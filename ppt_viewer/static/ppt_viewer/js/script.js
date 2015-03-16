/* jshint browser: true */

(function () {
  "use strict";
  var refreshThesis = function (section) {
        var request = new XMLHttpRequest();
        request.onreadystatechange = function () {
          if (request.readyState === 4 && request.status === 200) {
            document.getElementById("thesis").innerHTML = request.responseText;
          }
        };
        request.open("GET", "/thesis_list/" + section, true);
        request.send();
      },
      labels = document.getElementsByClassName("section"),
      addEvent = function () {
        refreshThesis(this.id);
      };
  for (var i = 0; i < labels.length; i++) {
    labels[i].addEventListener("click", addEvent, false);
  }
  if (labels.length > 0) refreshThesis(labels[0].id);
})();
