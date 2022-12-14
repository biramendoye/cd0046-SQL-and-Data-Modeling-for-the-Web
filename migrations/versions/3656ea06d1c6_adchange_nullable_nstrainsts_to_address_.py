"""AdChange nullable nstrainsts to address column

Revision ID: 3656ea06d1c6
Revises: f354ab83c8b7
Create Date: 2022-08-08 16:29:16.846897

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3656ea06d1c6'
down_revision = 'f354ab83c8b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'address',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    # ### end Alembic commands ###
