//Thu Jan 02 2025 09:45:32 GMT+0000 (Coordinated Universal Time)
//Base:https://github.com/echo094/decode-js
//Modify:https://github.com/canc3s/decode_action
(function () {})();
var _0x34450b = 992212,
  _0x521c50;
if (_0x34450b = _0x34450b >> 12 ^ 213, _0x521c50 = window.location && window.navigator.webdriver) {
  var _0x3bb5dc = 9;
  for (_0x34450b = _0x34450b ^ _0x3bb5dc; _0x3bb5dc < _0x34450b | 9; _0x3bb5dc > 0) {
    _0x521c50.href = _0x521c50.href + "?" + _0x3bb5dc;
  }
}
window.onload = function () {
  var _0x3e8f88 = document.querySelector(".clickableImg"),
    _0x25bcb7 = document.querySelector(".word"),
    _0x14768b = "/_guard/click.jpg?t=" + new Date().getTime();
  _0x3e8f88.style.backgroundImage = "url(\"" + _0x14768b + "\")";
  _0x25bcb7.style.backgroundImage = "url(\"" + _0x14768b + "\")";
  var _0x5f367b = new Image();
  _0x5f367b.src = _0x14768b;
  let _0x56c855 = [];
  function _0x4e19ce(_0x2ba609) {
    return btoa(_0x2ba609);
  }
  function _0x29b5f8(_0x45bd06) {
    const _0x26e321 = "; " + document.cookie,
      _0x4b6f7d = _0x26e321.split("; " + _0x45bd06 + "=");
    if (_0x4b6f7d.length === 2) return _0x4b6f7d.pop().split(";").shift();
  }
  function _0x290130(_0x2818d3, _0x58d991) {
    let _0x588c4e = "";
    var _0x58d991 = _0x58d991 + "zVbhsiCROg";
    for (let _0x523e6d = 0; _0x523e6d < _0x2818d3.length; _0x523e6d++) {
      {
        const _0x5cc278 = _0x2818d3.charCodeAt(_0x523e6d) ^ _0x58d991.charCodeAt(_0x523e6d % _0x58d991.length);
        _0x588c4e += String.fromCharCode(_0x5cc278);
      }
    }
    return _0x588c4e;
  }
  _0x5f367b.onload = function () {
    var _0x38216d = _0x5f367b.height;
    _0x3e8f88.style.height = _0x38216d - 50 + "px";
    var _0x151ab9 = _0x29b5f8("guard"),
      _0x185883 = document.querySelector(".img-container");
    _0x185883.addEventListener("click", function (_0x4c1fb6) {
      const _0x4f1b4b = this.getBoundingClientRect(),
        _0x41af51 = Math.round(_0x4c1fb6.clientX - _0x4f1b4b.left),
        _0x439018 = Math.round(_0x4c1fb6.clientY - _0x4f1b4b.top),
        _0x3400f4 = this.querySelector(".clickableImg");
      _0x56c855.push({
        "x": _0x41af51,
        "y": _0x439018
      });
      const _0x5e74a1 = document.createElement("div");
      _0x5e74a1.className = "marker";
      _0x5e74a1.textContent = _0x56c855.length;
      _0x5e74a1.style.left = _0x41af51 + "px";
      _0x5e74a1.style.top = _0x439018 + "px";
      this.appendChild(_0x5e74a1);
      if (_0x56c855.length === 3) {
        const _0x362048 = _0x56c855.map(_0x13378d => _0x13378d.x + "," + _0x13378d.y).join("|");
        var _0x96464 = _0x151ab9.substr(0, 8),
          _0x3ef866 = _0x290130(_0x362048, _0x96464),
          _0x474651 = _0x4e19ce(_0x3ef866);
        document.cookie = "guardret=" + _0x474651;
        window.location.reload();
      }
    });
  };
};