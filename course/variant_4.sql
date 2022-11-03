CREATE DATABASE candy_factory;

CREATE SCHEMA connections;

CREATE TABLE "buyer" (
	"buyer_id" integer PRIMARY KEY,
	"title text" NOT NULL,
	"phone" varchar(15) NULL,
);


CREATE TABLE "ingredient" (
	"ingredient_id" integer PRIMARY KEY,
	"title" text NOT NULL,
	"price" integer NOT NULL,
);


CREATE TABLE "product" (
	"product_id" integer PRIMARY KEY,
	"title text" NOT NULL,
	"description" text NOT NULL,
	"price" integer NOT NULL,
);


CREATE TABLE "provider" (
	"provide_id" integer PRIMARY KEY,
	"title" text NOT NULL,
	"phone" varchar(15) NOT NULL,
);

CREATE TABLE "buyer_product" (
	"buyer_id" integer REFERENCES buyer(buyer_id),
	"product_id" integer REFERENCES product(product_id),

	CONSTRAINT "buyer_product_pk" PRIMARY KEY (buyer_id, product_id)
);

CREATE TABLE "ingredient_providor" (
  "ingredient_id" integer REFERENCES ingredient(ingredient_id),
	"provider_id" integer REFERENCES provider(provider_id),

	CONSTRAINT "ingredient_providor_pk" PRIMARY KEY (ingredient_id, provider_id)
);

CREATE TABLE ingredient_product (
  "ingredient_id" integer REFERENCES ingredient(ingredient_id),
  "product_id" integer REFERENCES product(product_id),

	CONSTRAINT i"ngredient_product_pk" PRIMARY KEY (ingredient_id, product_id)
);

INSERT INTO product
VALUES
(1, "Корзиночка с малиной", "Корзиночка из песочного теста с кремом Маскарпоне и свежими ягодами милины", 110),
(2, "Корзиночка с клубникой", "Корзиночка из песочного теста с кремом Маскарпоне и свежими ягодами клубники", 90),
(3, "Корзиночка с ежевикой", "Корзиночка из песочного теста с кремом Маскарпоне и свежими ягодами ежевики", 100),
(4, "Корзиночка с голубикой", "Корзиночка из песочного теста с кремом Маскарпоне и свежими ягодами голубики", 100),
(5, "Корзиночка с ананасом", "Корзиночка из песочного теста с кремом Маскарпоне и свежими кусочками ананаса", 90);

INSERT INTO provider
VALUES
(1, "Ягоды от бабушки", "+74951473892"),
(2, "Вкусные корзиночки", "+74959735629"),
(3, "Фрукты всем нарадость", "+74956821464"),
(4, "Сладкие заготовки", "+74958845335");

INSERT INTO ingredient
VALUES
(1, "Малина", 30),
(2, "Клубника", 10),
(3, "Ежевика", 20),
(4, "Голубика", 20),
(5, "Ананас", 10),
(6, "Маскарпоне", 15),
(7, "Корзиночка", 10);

INSERT INTO buyer
VALUES
(1, "Булочки у Елены", "+79457747883"),
(2, "Сладости без гадостей", "+79459231425"),
(3, "Мир Ананасов", "+79457747883"),
(4, "Чай-чай-выруЧай", "+79456542971"),
(5, "ВикиХлебия", "+79459036450");

INSERT INTO buyer_product
VALUES
(1,2),
(1,3),
(1,5),
(2,3),
(2,4),
(3,5),
(4,1),
(4,2),
(4,5),
(5,1),
(5,5);

INSERT INTO ingredient_providor
VALUES
(1,1),
(2,1),
(3,1),
(4,1),
(5,3),
(6,4),
(7,4),
(7,2);

INSERT INTO ingredient_product
VALUES
(1,1),
(1,6),
(1,7),
(2,2),
(2,6),
(2,7),
(3,3),
(3,6),
(3,7),
(4,4),
(4,6),
(4,7),
(5,5),
(5,6),
(5,7);
