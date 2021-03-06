import { useContext } from "react";
import React from "react";
import { Route, Redirect } from "react-router-dom";
import { AuthContext } from "../Auth/Auth";

const PrivateRoute = ({ component: RouteComponent, ...rest }) => {
  let { currentUser } = useContext(AuthContext);
  return (
    <Route
      {...rest}
      render={(routeProps) =>
        !!currentUser ? (
          <RouteComponent {...routeProps} />
        ) : (
          <Redirect push to={"/login"} />
        )
      }
    />
  );
};

export default PrivateRoute;
