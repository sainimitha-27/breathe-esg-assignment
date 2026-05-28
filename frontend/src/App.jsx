function App() {
  const stats = [
    { title: "Total Records", value: 8 },
    { title: "Approved", value: 5 },
    { title: "Pending Review", value: 2 },
    { title: "Rejected", value: 1 },
    { title: "Suspicious", value: 2 },
  ];

  const records = [
    {
      category: "Fuel",
      activity: "Diesel Consumption",
      scope: "Scope 1",
      status: "Approved",
    },
    {
      category: "Electricity",
      activity: "Factory Electricity",
      scope: "Scope 2",
      status: "Suspicious",
    },
    {
      category: "Travel",
      activity: "Ground Transport",
      scope: "Scope 3",
      status: "Rejected",
    },
  ];

  return (
    <div style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>Breathe ESG Dashboard</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(5, 1fr)",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        {stats.map((item, index) => (
          <div
            key={index}
            style={{
              padding: "20px",
              border: "1px solid #ccc",
              borderRadius: "10px",
              textAlign: "center",
            }}
          >
            <h3>{item.title}</h3>
            <h2>{item.value}</h2>
          </div>
        ))}
      </div>

      <h2 style={{ marginTop: "50px" }}>Normalized ESG Records</h2>

      <table
        border="1"
        cellPadding="10"
        style={{
          width: "100%",
          marginTop: "20px",
          borderCollapse: "collapse",
        }}
      >
        <thead>
          <tr>
            <th>Category</th>
            <th>Activity</th>
            <th>Scope</th>
            <th>Status</th>
          </tr>
        </thead>

        <tbody>
          {records.map((record, index) => (
            <tr key={index}>
              <td>{record.category}</td>
              <td>{record.activity}</td>
              <td>{record.scope}</td>
              <td>{record.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;