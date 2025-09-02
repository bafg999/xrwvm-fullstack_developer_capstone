import LoginPanel from "./components/Login/Login"
import LoginPanel from "./components/registration/register"
import { Routes, Route } from "react-router-dom";

function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPanel />} />
      <Route path="/registration" element={<LoginPanel />} />
    </Routes>
  );
}
export default App;
