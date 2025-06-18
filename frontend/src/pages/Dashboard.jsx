export default function Dashboard() {
  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold">Crypto Escrow Portal</h1>
      <p className="mt-4">Welcome! Manage users, offers, wallets, and support here.</p>
      <div className="mt-8 p-4 bg-gray-100 rounded">
        <h2 className="text-xl font-semibold mb-2">Admin Dashboard</h2>
        <ul className="list-disc ml-6">
          <li>View platform stats (coming soon)</li>
          <li>Manage offers, users, and tickets (coming soon)</li>
          <li>Monitor wallet balances (coming soon)</li>
        </ul>
      </div>
    </div>
  );
}
