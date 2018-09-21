"""empty message

Revision ID: 7eee27e2db2e
Revises: ae61681548af
Create Date: 2018-06-14 13:54:44.720409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eee27e2db2e'
down_revision = 'ae61681548af'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adcode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=50), nullable=False),
    sa.Column('adcode', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('adcode')
    # ### end Alembic commands ###
