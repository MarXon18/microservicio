"""Migración Inicial

Revision ID: 7b8f030fe03d
Revises: 
Create Date: 2024-10-22 20:42:31.227543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b8f030fe03d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('catalogo',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=120), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.Column('activado', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nombre')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('catalogo')
    # ### end Alembic commands ###
