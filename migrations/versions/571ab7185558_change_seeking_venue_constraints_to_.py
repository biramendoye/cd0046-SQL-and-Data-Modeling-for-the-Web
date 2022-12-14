"""Change seeking_venue constraints to nullable

Revision ID: 571ab7185558
Revises: 82609e48bfba
Create Date: 2022-08-04 18:12:06.033129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '571ab7185558'
down_revision = '82609e48bfba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('artists', 'seeking_venue',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
