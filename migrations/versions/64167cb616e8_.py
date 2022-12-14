"""empty message

Revision ID: 64167cb616e8
Revises: 571ab7185558
Create Date: 2022-08-04 18:32:56.441790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64167cb616e8'
down_revision = '571ab7185558'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
