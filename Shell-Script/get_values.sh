function get_property {
	sed "/^$1 = /!d; s///" "$CONFIG" | wc -l
        sed "/^$1=/!d; s///" "$CONFIG" | wc -l
}
CONFIG=conflow.properties
NFLOW_DB_USER=$(get_property conflow.nflow.db.user)
echo $NFLOW_DB_USER
