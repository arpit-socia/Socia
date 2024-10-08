"""c

Revision ID: a392ecf44925
Revises: 50ffb0a7eef5
Create Date: 2024-09-28 18:47:47.766797

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = 'a392ecf44925'
down_revision = '50ffb0a7eef5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_business', sa.Column('refresh_token', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    op.add_column('user_public', sa.Column('refresh_token', sqlmodel.sql.sqltypes.AutoString(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_public', 'refresh_token')
    op.drop_column('user_business', 'refresh_token')
    # ### end Alembic commands ###
