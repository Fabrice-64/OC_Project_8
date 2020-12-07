

class ConnectToOFF:
    pass



class DataCleaning():

    def _check_special_characters(self, value):
        """
            Cleans the fields of the downloaded rows in order to avoid conflicts
            with mySQL syntax.
            Arguments:
                value: is a string to be checked.
            Returns:
                result: value cleaned from the various quotation marks
                or identified as empty.
        """
        if value is None or value == "":
            cleaned_value = "NaN"
        else:
            if '"' in value:
                value = value.replace('"', '')
            if "'" in value:
                value = value.replace("'", "\'")
            if "-" in value:
                value = value.replace("-", " ")
            if "'" in value:
                value.replace("\xc3\xa9", "é'")
            cleaned_value = value
        return cleaned_value

    def from_data_to_list(self, data, key_file, key_item):
        list_items = []
        items = data.get(key_file)
        for item in items:
            item = self._check_special_characters(item.get(key_item))
            if item != "NaN":
                list_items.append(item)
        return list_items

