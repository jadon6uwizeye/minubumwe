const routes = [
  {
    path: ["/", "/home"],
    exact: true,
    component: "Home",
  },
  {
    path: "/login",
    exact: true,
    component: "Login",
  },
  {
    path: "/register",
    exact: true,
    component: "Signup",
  }
];

export default routes;
