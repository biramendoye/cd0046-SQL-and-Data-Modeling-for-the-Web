"""Implement missing fields

Revision ID: 680d8df3440a
Revises: b8a5fd837003
Create Date: 2022-08-02 00:09:11.704272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '680d8df3440a'
down_revision = 'b8a5fd837003'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artists', sa.Column('website', sa.String(), nullable=True))
    op.add_column('artists', sa.Column('seeking_venue', sa.Boolean(), nullable=False))
    op.add_column('artists', sa.Column('seeking_description', sa.String(), nullable=True))
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('artists', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.add_column('venues', sa.Column('seeking_talent', sa.Boolean(), nullable=False))
    op.add_column('venues', sa.Column('seeking_description', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('website', sa.String(), nullable=True))
    op.add_column('venues', sa.Column('genres', sa.String(length=120), nullable=True))
    op.alter_column('venues', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venues', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('venues', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('venues', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('venues', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('venues', 'genres')
    op.drop_column('venues', 'website')
    op.drop_column('venues', 'seeking_description')
    op.drop_column('venues', 'seeking_talent')
    op.alter_column('artists', 'image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('artists', 'state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('artists', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('artists', 'seeking_description')
    op.drop_column('artists', 'seeking_venue')
    op.drop_column('artists', 'website')
    # ### end Alembic commands ###