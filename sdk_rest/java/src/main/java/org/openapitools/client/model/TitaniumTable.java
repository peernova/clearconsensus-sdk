/*
 * clearconsensus-sdk
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.TableColumn;
import org.openapitools.client.model.TitaniumTableRow;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonArray;
import com.google.gson.JsonDeserializationContext;
import com.google.gson.JsonDeserializer;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapterFactory;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

import org.openapitools.client.JSON;

/**
 * TitaniumTable
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2023-11-20T18:28:53.559516Z[UTC]")
public class TitaniumTable {
  public static final String SERIALIZED_NAME_COLUMNS = "columns";
  @SerializedName(SERIALIZED_NAME_COLUMNS)
  private List<TableColumn> columns = null;

  public static final String SERIALIZED_NAME_ROWS = "rows";
  @SerializedName(SERIALIZED_NAME_ROWS)
  private List<TitaniumTableRow> rows = null;

  public static final String SERIALIZED_NAME_TOTAL_ROWS = "totalRows";
  @SerializedName(SERIALIZED_NAME_TOTAL_ROWS)
  private String totalRows;

  public TitaniumTable() { 
  }

  public TitaniumTable columns(List<TableColumn> columns) {
    
    this.columns = columns;
    return this;
  }

  public TitaniumTable addColumnsItem(TableColumn columnsItem) {
    if (this.columns == null) {
      this.columns = new ArrayList<>();
    }
    this.columns.add(columnsItem);
    return this;
  }

   /**
   * Get columns
   * @return columns
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TableColumn> getColumns() {
    return columns;
  }


  public void setColumns(List<TableColumn> columns) {
    this.columns = columns;
  }


  public TitaniumTable rows(List<TitaniumTableRow> rows) {
    
    this.rows = rows;
    return this;
  }

  public TitaniumTable addRowsItem(TitaniumTableRow rowsItem) {
    if (this.rows == null) {
      this.rows = new ArrayList<>();
    }
    this.rows.add(rowsItem);
    return this;
  }

   /**
   * Get rows
   * @return rows
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<TitaniumTableRow> getRows() {
    return rows;
  }


  public void setRows(List<TitaniumTableRow> rows) {
    this.rows = rows;
  }


  public TitaniumTable totalRows(String totalRows) {
    
    this.totalRows = totalRows;
    return this;
  }

   /**
   * Get totalRows
   * @return totalRows
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getTotalRows() {
    return totalRows;
  }


  public void setTotalRows(String totalRows) {
    this.totalRows = totalRows;
  }



  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    TitaniumTable titaniumTable = (TitaniumTable) o;
    return Objects.equals(this.columns, titaniumTable.columns) &&
        Objects.equals(this.rows, titaniumTable.rows) &&
        Objects.equals(this.totalRows, titaniumTable.totalRows);
  }

  @Override
  public int hashCode() {
    return Objects.hash(columns, rows, totalRows);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class TitaniumTable {\n");
    sb.append("    columns: ").append(toIndentedString(columns)).append("\n");
    sb.append("    rows: ").append(toIndentedString(rows)).append("\n");
    sb.append("    totalRows: ").append(toIndentedString(totalRows)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }


  public static HashSet<String> openapiFields;
  public static HashSet<String> openapiRequiredFields;

  static {
    // a set of all properties/fields (JSON key names)
    openapiFields = new HashSet<String>();
    openapiFields.add("columns");
    openapiFields.add("rows");
    openapiFields.add("totalRows");

    // a set of required properties/fields (JSON key names)
    openapiRequiredFields = new HashSet<String>();
  }

 /**
  * Validates the JSON Object and throws an exception if issues found
  *
  * @param jsonObj JSON Object
  * @throws IOException if the JSON Object is invalid with respect to TitaniumTable
  */
  public static void validateJsonObject(JsonObject jsonObj) throws IOException {
      if (jsonObj == null) {
        if (TitaniumTable.openapiRequiredFields.isEmpty()) {
          return;
        } else { // has required fields
          throw new IllegalArgumentException(String.format("The required field(s) %s in TitaniumTable is not found in the empty JSON string", TitaniumTable.openapiRequiredFields.toString()));
        }
      }

      Set<Entry<String, JsonElement>> entries = jsonObj.entrySet();
      // check to see if the JSON string contains additional fields
      for (Entry<String, JsonElement> entry : entries) {
        if (!TitaniumTable.openapiFields.contains(entry.getKey())) {
          throw new IllegalArgumentException(String.format("The field `%s` in the JSON string is not defined in the `TitaniumTable` properties. JSON: %s", entry.getKey(), jsonObj.toString()));
        }
      }
      JsonArray jsonArraycolumns = jsonObj.getAsJsonArray("columns");
      if (jsonArraycolumns != null) {
        // ensure the json data is an array
        if (!jsonObj.get("columns").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `columns` to be an array in the JSON string but got `%s`", jsonObj.get("columns").toString()));
        }

        // validate the optional field `columns` (array)
        for (int i = 0; i < jsonArraycolumns.size(); i++) {
          TableColumn.validateJsonObject(jsonArraycolumns.get(i).getAsJsonObject());
        };
      }
      JsonArray jsonArrayrows = jsonObj.getAsJsonArray("rows");
      if (jsonArrayrows != null) {
        // ensure the json data is an array
        if (!jsonObj.get("rows").isJsonArray()) {
          throw new IllegalArgumentException(String.format("Expected the field `rows` to be an array in the JSON string but got `%s`", jsonObj.get("rows").toString()));
        }

        // validate the optional field `rows` (array)
        for (int i = 0; i < jsonArrayrows.size(); i++) {
          TitaniumTableRow.validateJsonObject(jsonArrayrows.get(i).getAsJsonObject());
        };
      }
      if (jsonObj.get("totalRows") != null && !jsonObj.get("totalRows").isJsonPrimitive()) {
        throw new IllegalArgumentException(String.format("Expected the field `totalRows` to be a primitive type in the JSON string but got `%s`", jsonObj.get("totalRows").toString()));
      }
  }

  public static class CustomTypeAdapterFactory implements TypeAdapterFactory {
    @SuppressWarnings("unchecked")
    @Override
    public <T> TypeAdapter<T> create(Gson gson, TypeToken<T> type) {
       if (!TitaniumTable.class.isAssignableFrom(type.getRawType())) {
         return null; // this class only serializes 'TitaniumTable' and its subtypes
       }
       final TypeAdapter<JsonElement> elementAdapter = gson.getAdapter(JsonElement.class);
       final TypeAdapter<TitaniumTable> thisAdapter
                        = gson.getDelegateAdapter(this, TypeToken.get(TitaniumTable.class));

       return (TypeAdapter<T>) new TypeAdapter<TitaniumTable>() {
           @Override
           public void write(JsonWriter out, TitaniumTable value) throws IOException {
             JsonObject obj = thisAdapter.toJsonTree(value).getAsJsonObject();
             elementAdapter.write(out, obj);
           }

           @Override
           public TitaniumTable read(JsonReader in) throws IOException {
             JsonObject jsonObj = elementAdapter.read(in).getAsJsonObject();
             validateJsonObject(jsonObj);
             return thisAdapter.fromJsonTree(jsonObj);
           }

       }.nullSafe();
    }
  }

 /**
  * Create an instance of TitaniumTable given an JSON string
  *
  * @param jsonString JSON string
  * @return An instance of TitaniumTable
  * @throws IOException if the JSON string is invalid with respect to TitaniumTable
  */
  public static TitaniumTable fromJson(String jsonString) throws IOException {
    return JSON.getGson().fromJson(jsonString, TitaniumTable.class);
  }

 /**
  * Convert an instance of TitaniumTable to an JSON string
  *
  * @return JSON string
  */
  public String toJson() {
    return JSON.getGson().toJson(this);
  }
}

