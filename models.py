class Visitor(Base):
    __tablename__ = "visitors"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True)
    port = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    country = Column(String, nullable=True)
    region = Column(String, nullable=True)
    city = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
