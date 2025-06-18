import { ClerkProvider } from '@clerk/clerk-react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from './pages/Dashboard';
import Offers from './pages/Offers';
import Wallets from './pages/Wallets';
import Fees from './pages/Fees';
import Support from './pages/Support';

function App() {
  return (
    <ClerkProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/offers" element={<Offers />} />
          <Route path="/wallets" element={<Wallets />} />
          <Route path="/fees" element={<Fees />} />
          <Route path="/support" element={<Support />} />
        </Routes>
      </BrowserRouter>
    </ClerkProvider>
  );
}

export default App;
