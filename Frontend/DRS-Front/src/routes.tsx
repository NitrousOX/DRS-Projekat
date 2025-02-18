import { createBrowserRouter, RouterProvider } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import HomePage from "./pages/HomePage";
import RegistrationListPage from "./pages/RegistrationListPage";
import NotFoundPage from "./pages/NotFoundPage";




const router = createBrowserRouter([
    {
        path: "/login",
        element: <LoginPage />,
      },
      {
        path: "/register",
        element: <RegisterPage />,
      },
      
      // Routes with the MainLayout
      {
        element: <MainLayout />, 
        children: [
          {
            path: "/",
            element: <HomePage />,
          },
          {
            path: "/registration-list",
            element: <RegistrationListPage />,
          },
        ],
      },
    
      // Catch-all route (404)
      {
        path: "*",
        element: <NotFoundPage />,
      },
]);

export default function AppRoutes() {
    return <RouterProvider router={router} />;
}