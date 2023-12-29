"""added cascade

Revision ID: e6ee993f206c
Revises: 97a3c2fe5ec2
Create Date: 2023-12-29 12:06:10.060473

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e6ee993f206c"
down_revision: Union[str, None] = "97a3c2fe5ec2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "order_product_link",
        sa.Column("fixed_price", sa.Integer(), server_default="0", nullable=False),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("order_product_link", "fixed_price")
    # ### end Alembic commands ###
