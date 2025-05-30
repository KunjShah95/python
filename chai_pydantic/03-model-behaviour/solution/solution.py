from pydantic import BaseModel, Field,field_validator, model_validator, computed_field

class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int = Field(..., ge=1)
    rate_per_night:float
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
    @field_validator('nights')
    def validate_nights(cls, value):
        if value < 1:
            raise ValueError('Nights must be at least 1')
        return value
    
    @model_validator(mode='after')
    def validate_booking(cls, values):
        if values.nights < 1:
            raise ValueError('Booking must be for at least one night')
        return values
    
# Example usage
booking = Booking(user_id=123, room_id=456, nights=3, rate_per_night=100.0)
print(booking)
print(f'Total Amount: {booking.total_amount}')