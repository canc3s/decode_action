//Thu Aug 15 2024 11:03:11 GMT+0000 (Coordinated Universal Time)
//Base:https://github.com/echo094/decode-js
//Modify:https://github.com/smallfawn/decode_action
(function () {})();
var oooo = 992212,
  ooe;
if (oooo = oooo >> 12 ^ 213, ooe = window.location && window.navigator.webdriver) {
  var i = 9;
  for (oooo = oooo ^ i; i < oooo | 9; i > 0) {
    ooe.href = ooe.href + "?" + i;
  }
}
var btn = document.getElementById("access");
"ontouchstart" in window ? btn.addEventListener("touchstart", function (_0x37496e) {
  var isTrusted = _0x37496e.isTrusted;
  if (isTrusted) {
    var _0x113711 = _0x37496e.clientX;
    var _0x1f5e70 = _0x37496e.clientY;
    var _0x28ab4f = _0x113711 + _0x1f5e70 + 2;
    var data = {
      "x": _0x113711,
      "y": _0x1f5e70,
      "a": _0x28ab4f
    };
    t(data);
  }
}) : btn.addEventListener("click", function (_0x2e1e62) {
  var isTrusted = _0x2e1e62.isTrusted;
  if (isTrusted) {
    var _0x7a3071 = _0x2e1e62.clientX;
    var _0x428a5b = _0x2e1e62.clientY;
    var _0x3402b4 = _0x7a3071 + _0x428a5b + 2;
    var data = {
      "x": _0x7a3071,
      "y": _0x428a5b,
      "a": _0x3402b4
    };
    t(data);
  }
});
function b(input) {
  return btoa(input);
}
function x(input, _0x393591) {
  let output = "";
  var _0x393591 = _0x393591 + "PTNo2n3Ev5";
  for (let _0x5a73f4 = 0; _0x5a73f4 < input.length; _0x5a73f4++) {
    const charCode = input.charCodeAt(_0x5a73f4) ^ _0x393591.charCodeAt(_0x5a73f4 % _0x393591.length);
    output += String.fromCharCode(charCode);
  }
  return output;
}
function gc(_0x5b8b9e) {
  var _0x1b0ed1 = "; " + document.cookie,
    parts = _0x1b0ed1.split("; " + _0x5b8b9e + "=");
  if (parts.length == 2) return parts.pop().split(";").shift();
}
function setRet(_0x113992, data) {
  var _0x408072 = _0x113992.substr(0, 8),
    encrypted = x(JSON.stringify(data), _0x408072),
    encode = b(encrypted);
  if (typeof window === "undefined") {
    encode = encode.split("").reverse().join("");
  }
  document.cookie = "guardret=" + encode;
  window.location.reload();
}
function t(data) {
  var _0x3ad255 = gc("guard");
  !_0x3ad255 ? window.location.reload() : setRet(_0x3ad255, data);
}