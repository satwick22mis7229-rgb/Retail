import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid
} from "recharts";

const data = [
  { month: "Jan", revenue: 10000 },
  { month: "Feb", revenue: 15000 },
  { month: "Mar", revenue: 25000 },
  { month: "Apr", revenue: 40000 },
];

function RevenueChart() {
  return (
    <BarChart width={600} height={300} data={data}>
      <CartesianGrid strokeDasharray="3 3" />
      <XAxis dataKey="month" />
      <YAxis />
      <Tooltip />
      <Bar dataKey="revenue" />
    </BarChart>
  );
}

export default RevenueChart;