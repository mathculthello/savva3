(window["webpackJsonp"] = window["webpackJsonp"] || []).push([[0],{

/***/ "./webpack-src/Base/client.js":
/*!************************************!*\
  !*** ./webpack-src/Base/client.js ***!
  \************************************/
/*! exports provided: default */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var apollo_client__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! apollo-client */ "./node_modules/apollo-client/index.js");
/* harmony import */ var apollo_link_http__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! apollo-link-http */ "./node_modules/apollo-link-http/lib/index.js");
/* harmony import */ var apollo_cache_inmemory__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! apollo-cache-inmemory */ "./node_modules/apollo-cache-inmemory/lib/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! react */ "./node_modules/react/index.js");
/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_3___default = /*#__PURE__*/__webpack_require__.n(react__WEBPACK_IMPORTED_MODULE_3__);




var client = new apollo_client__WEBPACK_IMPORTED_MODULE_0__["ApolloClient"]({
  // By default, this client will send queries to the
  //  `/graphql` endpoint on the same host
  // Pass the configuration option { uri: YOUR_GRAPHQL_API_URL } to the `HttpLink` to connect
  // to a different host
  link: new apollo_link_http__WEBPACK_IMPORTED_MODULE_1__["HttpLink"](),
  cache: new apollo_cache_inmemory__WEBPACK_IMPORTED_MODULE_2__["InMemoryCache"]()
});
/* harmony default export */ __webpack_exports__["default"] = (client);

/***/ })

}]);
//# sourceMappingURL=0.js.map