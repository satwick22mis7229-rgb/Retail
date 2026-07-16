"""Create module 2 retail intelligence schema

Revision ID: 20260716_0001
Revises:
Create Date: 2026-07-16 10:20:00
"""

from alembic import op
import sqlalchemy as sa


revision = "20260716_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("address", sa.String(), nullable=True),
        sa.Column("segment", sa.String(), nullable=False, server_default="general"),
        sa.Column("loyalty_tier", sa.String(), nullable=False, server_default="standard"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_customers_id"), "customers", ["id"], unique=False)

    op.create_table(
        "stores",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("manager_name", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("code"),
    )
    op.create_index(op.f("ix_stores_id"), "stores", ["id"], unique=False)

    op.create_table(
        "suppliers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("phone", sa.String(), nullable=True),
        sa.Column("address", sa.String(), nullable=True),
        sa.Column("lead_time_days", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("reliability_score", sa.Float(), nullable=False, server_default="0"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_suppliers_id"), "suppliers", ["id"], unique=False)

    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=False)

    op.create_table(
        "alerts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("alert_type", sa.String(), nullable=False),
        sa.Column("severity", sa.String(), nullable=False, server_default="medium"),
        sa.Column("status", sa.String(), nullable=False, server_default="open"),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("message", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["store_id"], ["stores.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_alerts_id"), "alerts", ["id"], unique=False)

    op.create_table(
        "warehouses",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=True),
        sa.Column("capacity", sa.Float(), nullable=False, server_default="0"),
        sa.Column("utilization_rate", sa.Float(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["store_id"], ["stores.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_warehouses_id"), "warehouses", ["id"], unique=False)

    op.create_table(
        "products",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("sku", sa.String(), nullable=False),
        sa.Column("category", sa.String(), nullable=False, server_default="general"),
        sa.Column("price", sa.Float(), nullable=False),
        sa.Column("cost_price", sa.Float(), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("safety_stock", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("reorder_point", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("reorder_quantity", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("is_active", sa.Boolean(), nullable=False, server_default=sa.text("true")),
        sa.Column("preferred_supplier_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["preferred_supplier_id"], ["suppliers.id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("sku"),
    )
    op.create_index(op.f("ix_products_id"), "products", ["id"], unique=False)

    op.create_table(
        "digital_twin_snapshots",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("snapshot_payload", sa.JSON(), nullable=False),
        sa.Column("snapshot_version", sa.String(), nullable=False, server_default="v1"),
        sa.Column("state_hash", sa.String(), nullable=True),
        sa.Column("created_by", sa.String(), nullable=False, server_default="system"),
        sa.Column("captured_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["store_id"], ["stores.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_digital_twin_snapshots_id"), "digital_twin_snapshots", ["id"], unique=False)
    op.create_index("ix_digital_twin_snapshots_state_hash", "digital_twin_snapshots", ["state_hash"], unique=False)

    op.create_table(
        "simulation_runs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("store_id", sa.Integer(), nullable=False),
        sa.Column("scenario_name", sa.String(), nullable=False),
        sa.Column("scenario_payload", sa.JSON(), nullable=False),
        sa.Column("result_payload", sa.JSON(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["store_id"], ["stores.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_simulation_runs_id"), "simulation_runs", ["id"], unique=False)

    op.create_table(
        "supplier_performance",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("supplier_id", sa.Integer(), nullable=False),
        sa.Column("measured_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("on_time_delivery_rate", sa.Float(), nullable=False, server_default="0"),
        sa.Column("average_lead_time_days", sa.Float(), nullable=False, server_default="0"),
        sa.Column("defect_rate", sa.Float(), nullable=False, server_default="0"),
        sa.Column("delay_incidents", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["supplier_id"], ["suppliers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_supplier_performance_id"), "supplier_performance", ["id"], unique=False)

    op.create_table(
        "purchase_orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("supplier_id", sa.Integer(), nullable=False),
        sa.Column("warehouse_id", sa.Integer(), nullable=False),
        sa.Column("status", sa.String(), nullable=False, server_default="pending"),
        sa.Column("ordered_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("expected_delivery_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("total_amount", sa.Float(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["supplier_id"], ["suppliers.id"]),
        sa.ForeignKeyConstraint(["warehouse_id"], ["warehouses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_purchase_orders_id"), "purchase_orders", ["id"], unique=False)

    op.create_table(
        "recommendations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("supplier_id", sa.Integer(), nullable=True),
        sa.Column("recommendation_type", sa.String(), nullable=False),
        sa.Column("priority", sa.String(), nullable=False, server_default="medium"),
        sa.Column("confidence_score", sa.Float(), nullable=False, server_default="0"),
        sa.Column("rationale", sa.Text(), nullable=False),
        sa.Column("execution_status", sa.String(), nullable=False, server_default="pending"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"]),
        sa.ForeignKeyConstraint(["supplier_id"], ["suppliers.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_recommendations_id"), "recommendations", ["id"], unique=False)

    op.create_table(
        "shelves",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("warehouse_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("zone", sa.String(), nullable=False, server_default="general"),
        sa.Column("capacity", sa.Integer(), nullable=False, server_default="0"),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"]),
        sa.ForeignKeyConstraint(["warehouse_id"], ["warehouses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_shelves_id"), "shelves", ["id"], unique=False)

    op.create_table(
        "demand_forecasts",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("forecast_date", sa.Date(), nullable=False),
        sa.Column("predicted_units", sa.Float(), nullable=False),
        sa.Column("confidence_score", sa.Float(), nullable=False, server_default="0"),
        sa.Column("model_name", sa.String(), nullable=False, server_default="baseline"),
        sa.Column("model_version", sa.String(), nullable=False, server_default="v1"),
        sa.Column("forecast_horizon", sa.Integer(), nullable=False, server_default="1"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_demand_forecasts_id"), "demand_forecasts", ["id"], unique=False)

    op.create_table(
        "inventory",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("warehouse_id", sa.Integer(), nullable=False),
        sa.Column("shelf_id", sa.Integer(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("reserved_quantity", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("reorder_threshold", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("stockout_risk", sa.Float(), nullable=False, server_default="0"),
        sa.Column("status", sa.String(), nullable=False, server_default="in_stock"),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"]),
        sa.ForeignKeyConstraint(["shelf_id"], ["shelves.id"]),
        sa.ForeignKeyConstraint(["warehouse_id"], ["warehouses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_inventory_id"), "inventory", ["id"], unique=False)

    op.create_table(
        "sales",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("customer_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("warehouse_id", sa.Integer(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("unit_price", sa.Float(), nullable=False, server_default="0"),
        sa.Column("total_amount", sa.Float(), nullable=False, server_default="0"),
        sa.Column("sold_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.ForeignKeyConstraint(["customer_id"], ["customers.id"]),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"]),
        sa.ForeignKeyConstraint(["warehouse_id"], ["warehouses.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_sales_id"), "sales", ["id"], unique=False)

    op.create_table(
        "inventory_events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("inventory_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("event_type", sa.String(), nullable=False),
        sa.Column("quantity_change", sa.Integer(), nullable=False),
        sa.Column("unit_cost", sa.Float(), nullable=False, server_default="0"),
        sa.Column("event_timestamp", sa.DateTime(timezone=True), nullable=False, server_default=sa.text("now()")),
        sa.Column("reason", sa.String(), nullable=True),
        sa.ForeignKeyConstraint(["inventory_id"], ["inventory.id"]),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_inventory_events_id"), "inventory_events", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_inventory_events_id"), table_name="inventory_events")
    op.drop_table("inventory_events")
    op.drop_index(op.f("ix_sales_id"), table_name="sales")
    op.drop_table("sales")
    op.drop_index(op.f("ix_inventory_id"), table_name="inventory")
    op.drop_table("inventory")
    op.drop_index(op.f("ix_demand_forecasts_id"), table_name="demand_forecasts")
    op.drop_table("demand_forecasts")
    op.drop_index(op.f("ix_shelves_id"), table_name="shelves")
    op.drop_table("shelves")
    op.drop_index(op.f("ix_recommendations_id"), table_name="recommendations")
    op.drop_table("recommendations")
    op.drop_index(op.f("ix_purchase_orders_id"), table_name="purchase_orders")
    op.drop_table("purchase_orders")
    op.drop_index(op.f("ix_supplier_performance_id"), table_name="supplier_performance")
    op.drop_table("supplier_performance")
    op.drop_index(op.f("ix_simulation_runs_id"), table_name="simulation_runs")
    op.drop_table("simulation_runs")
    op.drop_index("ix_digital_twin_snapshots_state_hash", table_name="digital_twin_snapshots")
    op.drop_index(op.f("ix_digital_twin_snapshots_id"), table_name="digital_twin_snapshots")
    op.drop_table("digital_twin_snapshots")
    op.drop_index(op.f("ix_products_id"), table_name="products")
    op.drop_table("products")
    op.drop_index(op.f("ix_warehouses_id"), table_name="warehouses")
    op.drop_table("warehouses")
    op.drop_index(op.f("ix_alerts_id"), table_name="alerts")
    op.drop_table("alerts")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_suppliers_id"), table_name="suppliers")
    op.drop_table("suppliers")
    op.drop_index(op.f("ix_stores_id"), table_name="stores")
    op.drop_table("stores")
    op.drop_index(op.f("ix_customers_id"), table_name="customers")
    op.drop_table("customers")
