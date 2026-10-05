import random
from datetime import datetime, timedelta

class DataService:
    """
    Generates dynamic analytics and server performance data 
    based on user selected parameters without needing a database.
    """

    REGIONAL_MULTIPLIERS = {
        "global": 1.0,
        "us-east": 1.35,
        "eu-west": 0.95,
        "ap-south": 1.15
    }

    @classmethod
    def get_filtered_data(cls, region="global", days=7, performance_mode="standard"):
        multiplier = cls.REGIONAL_MULTIPLIERS.get(region, 1.0)
        
        # Adjust multiplier based on performance mode
        if performance_mode == "turbo":
            multiplier *= 1.4
        elif performance_mode == "eco":
            multiplier *= 0.75

        # Base values affected by user inputs
        base_users = int(12500 * multiplier)
        base_revenue = round(45200.00 * multiplier, 2)
        avg_response_time = round(120 / (multiplier if multiplier > 0 else 1), 1)
        system_health = min(99.9, round(98.5 + (0.5 * random.random()), 2))

        # Generate daily trend data for charts based on 'days' parameter
        chart_labels = []
        user_trend = []
        revenue_trend = []
        
        today = datetime.now()
        for i in range(days - 1, -1, -1):
            date_str = (today - timedelta(days=i)).strftime("%b %d")
            chart_labels.append(date_str)
            
            # Add dynamic variance
            daily_user = int((base_users / days) * random.uniform(0.85, 1.15))
            daily_rev = round((base_revenue / days) * random.uniform(0.80, 1.20), 2)
            
            user_trend.append(daily_user)
            revenue_trend.append(daily_rev)

        return {
            "status": "success",
            "filters_applied": {
                "region": region,
                "days": days,
                "performance_mode": performance_mode
            },
            "metrics": {
                "total_users": base_users,
                "total_revenue": f"${base_revenue:,.2f}",
                "avg_response_time": f"{avg_response_time}ms",
                "system_health": f"{system_health}%"
            },
            "chart_data": {
                "labels": chart_labels,
                "users": user_trend,
                "revenue": revenue_trend
            },
            "logs": [
                {"time": datetime.now().strftime("%H:%M:%S"), "event": f"Applied '{region.upper()}' region filters."},
                {"time": datetime.now().strftime("%H:%M:%S"), "event": f"Engine operating in '{performance_mode}' mode."},
                {"time": datetime.now().strftime("%H:%M:%S"), "event": f"Calculated telemetry across last {days} days."}
            ]
        }
