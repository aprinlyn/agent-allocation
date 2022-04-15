from enum import unique
from xmlrpc.client import Boolean, DateTime
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base


class Agent(Base):
    __tablename__ = "agents"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(20), index=True, nullable=False)
    email       = Column(String, nullable=False)
    qismo_agent_id = Column(Integer, index=True, nullable=False)
    is_active   = Column(String, nullable=False)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
    updated_at  = Column(DateTime(timezone=True), onupdate=func.now())
    user_agent  = relationship("UserAgent", primaryjoin="UserAgent.agent_id == Agent.id", cascade="all, delete-orphan")
    def __repr__(self):
        return 'Agent(name=%s, email=%s, qismo_agent_id=%s, is_active=%s, created_at=%s, updated_at=%s)' % (self.name, self.email, self.qismo_agent_id, self.is_active, self.created_at, self.updated_at)

class User(Base):
    __tablename__ = "users"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(20), index=True, nullable=False)
    email       = Column(String, nullable=True)
    qismo_user_id = Column(Integer, index=True, nullable=False)
    is_resolve  = Column(String, nullable=False)
    app_id      = Column(Integer, nullable=False)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
    updated_at  = Column(DateTime(timezone=True), onupdate=func.now())
    user_agent  = relationship("UserAgent", primaryjoin="UserAgent.user_id == User.id", cascade="all, delete-orphan")
    def __repr__(self):
        return 'User(name=%s, email=%s, qismo_user_id=%s, is_resolve=%s, app_id=%s, created_at=%s, updated_at=%s)' % (self.name, self.email, self.qismo_user_id, self.is_resolve, self.app_id, self.created_at, self.updated_at)

class UserAgent(Base):
    __tablename__ = "user_agents"

    id          = Column(Integer, primary_key=True, index=True)
    room_id     = Column(Integer, index=True, nullable=False)
    agent_id    = Column(Integer, ForeignKey('users.id'), nullable=False)
    user_id     = Column(Integer, ForeignKey('agents.id'), nullable=False)
    def __repr__(self):
        return 'UserAgent(room_id=%s, agent_id=%s, user_id=%s)' % (self.room_id, self.agent_id, self.user_id)