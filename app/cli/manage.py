import argparse
import asyncio

from sqlalchemy import update

from app.db.session import SessionLocal
from app.models.entities import User


async def deactivate_user(user_id: int) -> None:
    async with SessionLocal() as db:
        await db.execute(update(User).where(User.id == user_id).values(is_active=False))
        await db.commit()


def main() -> None:
    parser = argparse.ArgumentParser(description="Admin CLI for Telegram Python clone")
    subparsers = parser.add_subparsers(dest="command", required=True)

    deactivate = subparsers.add_parser("deactivate-user", help="Deactivate user account")
    deactivate.add_argument("user_id", type=int)

    args = parser.parse_args()

    if args.command == "deactivate-user":
        asyncio.run(deactivate_user(args.user_id))


if __name__ == "__main__":
    main()
