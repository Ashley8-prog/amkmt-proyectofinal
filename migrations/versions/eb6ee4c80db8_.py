"""empty message

<<<<<<<< HEAD:migrations/versions/eb6ee4c80db8_.py
Revision ID: eb6ee4c80db8
Revises: 
Create Date: 2023-09-27 19:22:02.606455
========
Revision ID: 1424dbe0cfa6
Revises: 
Create Date: 2023-09-27 23:42:37.421756
>>>>>>>> d24d48427a2a623cf83bd845e2539850b6a694fa:migrations/versions/1424dbe0cfa6_.py

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
<<<<<<<< HEAD:migrations/versions/eb6ee4c80db8_.py
revision = 'eb6ee4c80db8'
========
revision = '1424dbe0cfa6'
>>>>>>>> d24d48427a2a623cf83bd845e2539850b6a694fa:migrations/versions/1424dbe0cfa6_.py
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('product_image_url', sa.String(length=255), nullable=False),
    sa.Column('price', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=400), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tokenblocked',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('phone', sa.String(length=150), nullable=False),
    sa.Column('salt', sa.String(length=180), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('reservas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reservacion_date', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('cantidad_personas', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservas')
    op.drop_table('user')
    op.drop_table('tokenblocked')
    op.drop_table('products')
    # ### end Alembic commands ###
