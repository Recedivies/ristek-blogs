// Reducers
// import Signup from "./components/signup/Signup";
// import Login from "./components/login/Login";

import { composeWithDevTools } from "redux-devtools-extension";
import { combineReducers, createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";

const reducer = combineReducers({
  // signup: Signup,
  // login: Login,
});

export const store = createStore(
  reducer,
  composeWithDevTools(applyMiddleware(thunk))
);
