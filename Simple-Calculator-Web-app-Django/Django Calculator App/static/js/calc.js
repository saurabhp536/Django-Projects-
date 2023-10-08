var numKeys = [];
var opns = [];
var res = document.querySelector("#resultArea");
var clrBtn = document.querySelector("#clrTxt");
var delBtn = document.querySelector("#del");
var eqBtn = document.querySelector("#eq");
var decPoint = document.querySelector("#decp");
var opnSyms = ["+", "-", "*", "/"];

// Function to update the result area
function updateResult(value) {
  res.textContent += value;
}

// Add click event listeners to number buttons
for (var i = 0; i <= 9; i++) {
  (function (i) {
    qs = "#num" + i;
    numKeys.push(document.querySelector(qs));
    numKeys[i].addEventListener("click", function () {
      updateResult(i);
    });
  })(i);
}

// Add click event listeners to operator buttons
for (var i = 0; i <= 3; i++) {
  (function (i) {
    qs = "#op" + i;
    opns.push(document.querySelector(qs));
    opns[i].addEventListener("click", function () {
      updateResult(opnSyms[i]);
    });
  })(i);
}

// Clear button event listener
clrBtn.addEventListener("click", function () {
  res.textContent = "";
});

// Delete button event listener
delBtn.addEventListener("click", function () {
  res.textContent = res.textContent.substring(0, res.textContent.length - 1);
});

// Decimal point button event listener
decPoint.addEventListener("click", function () {
  // Check if a decimal point already exists
  if (res.textContent.indexOf(".") === -1) {
    updateResult(".");
  }
});

// Equal button event listener
eqBtn.addEventListener("click", function () {
  try {
    var result = eval(res.textContent);
    if (isNaN(result) || !isFinite(result)) {
      res.textContent = "Error";
    } else {
      res.textContent = result;
    }
  } catch (e) {
    res.textContent = "Error";
  }
});
